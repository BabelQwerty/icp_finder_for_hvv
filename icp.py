import requests , sys , logging , inspect
from parsel import Selector
from functools import wraps
from datetime import datetime
from urllib.parse import urljoin,urlparse,quote
from sys import argv
from tldextract import extract as domain_extract

_mapper_dict = {
    1:"companyName",
    2:"boss",
    3:"money",
    4:"BaiFenBi",
    5:"date",
    0:"YingYeQingKuang"
}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

_FenZhiJiGou = []


class ColoredFormatter(logging.Formatter):
    colors = {'black': 30,'red': 31,'green': 32,'yellow': 33,'blue': 34,'magenta': 35,'cyan': 36,'white': 37,'bgred': 41,'bggrey': 100 }
    mapping = {'INFO': 'cyan','WARNING': 'yellow','ERROR': 'red','CRITICAL': 'bgred','DEBUG': 'bggrey','SUCCESS': 'green'}
    prefix = '\033['
    suffix = '\033[0m'

    def colored(self, text, color=None):
        if color not in self.colors: color = 'white'
        return (self.prefix+'%dm%s'+self.suffix) % (self.colors[color], text)

    def format(self, record):
        log_fmt = self.colored(record.levelname, self.mapping.get(record.levelname, 'white'))+" - %(asctime)s - process: %(process)d - %(filename)s - %(name)s - %(lineno)d - %(module)s - %(message)s"
        return logging.Formatter(log_fmt).format(record)

def add_level(logger , level_name , level_num = 25  , cf_instance = ColoredFormatter() , cus_color = 100 ):
    handler = logging.StreamHandler()
    handler.setFormatter(cf_instance)
    level_name = level_name.upper()
    _low_level_name = level_name.lower()
    cf_instance.mapping.update({ level_name : 'custom_add' })
    cf_instance.colors.update({'custom_add':cus_color})
    logging.level_name = level_num
    logging.addLevelName(logging.level_name , level_name )
    setattr(logger ,_low_level_name ,  lambda message, *args: logger._log(logging.level_name, message, args))
    return logger

def get_filepath():
    """
    return {file}.log
    """
    filename = f"{'.'.join([i[1] for i in inspect.getouterframes(inspect.currentframe() , 2 ) ][-1].split('.')[:-1]) if '.'.join([i[1] for i in inspect.getouterframes(inspect.currentframe() , 2 ) ][-1].split('.')[:-1]) != '' else [i[1] for i in inspect.getouterframes(inspect.currentframe() , 2 ) ][-1].split('/')[-1]}"  + ".log"
    return f"{'.'.join(filename.split('.')[:-1])}.log"

def enable_filelog(logger , file_path = get_filepath()  ):
    file_handler = logging.FileHandler(filename = file_path,
            mode='a',
            encoding=None,
            delay=False,
            errors=None)
    file_format =  logging.Formatter("%(levelname)s - %(asctime)s - process: %(process)d - %(filename)s - %(name)s - %(lineno)d - %(module)s - %(message)s")
    file_handler.setLevel(level=logging.DEBUG)
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler )
    return logger

#  file_path = get_filepath()
def getLogger():
    """
    enable_filelog : filelog Flag(default False)
    file_path filelog path , default is {file}.log
    """
    # exec_file = [i[1] for i in inspect.getouterframes(inspect.currentframe() , 2 ) ][-1]
    exec_file = [i[1] for i in inspect.getouterframes(inspect.currentframe() , 2 ) ][-1].split('/')[-1].split('.')[0]
    logger = logging.getLogger(exec_file)
    handler = logging.StreamHandler()
    handler.setFormatter(ColoredFormatter())
    logger.addHandler(handler)
    logging.SUCCESS = 25 
    logging.addLevelName(logging.SUCCESS, 'SUCCESS')
    setattr(logger, 'success', lambda message, *args: logger._log(logging.SUCCESS, message, args))
    logger.setLevel(logging.INFO)
    return logger

def task_wrap(wrap_func , num = 60):
    @wraps(wrap_func)
    def _wrap_func(*args, **kwargs):
        def handle(signum, frame): # 收到信号 SIGALRM 后的回调函数，第一个参数是信号的数字，第二个参数是the interrupted stack frame.
            raise RuntimeError
        t1 = datetime.now()
        logger.debug(f"<{wrap_func.__name__}> start {t1.strftime('%d/%m/%y %H:%M:%S.%f')}")
        try:
            _result = wrap_func(*args , **kwargs)
            return _result
        except Exception as e:
            logger.warning(f"<{wrap_func.__name__} {e.args}>")
            import traceback
            traceback.format_exc()
        finally:
            t2 = datetime.now()
            logger.debug(f"<{wrap_func.__name__}> finish {t2.strftime('%d/%m/%y %H:%M:%S.%f')}")
            time_cost  = t2 - t1 
            logger.debug(f"<{wrap_func.__name__}> cost {time_cost.seconds} second ")
    return _wrap_func

def get_FenZiJiGou(  sel):
    
    from_company = sel.xpath("//html/body/div[3]/div[2]/div/div[1]/div[1]/text()").extract()[0]
    _ = {}
    __ = []
    result = []
    for index , value in enumerate( sel.xpath("//html/body/div[3]/div[4]/div[1]/table[4]/tbody/tr/td/*/node()")):
        _.update({_mapper_dict.get((index+1)%6) : value.extract()})
        if (index+1) %  6 == 0 and index > 0:
            __.append(_)
            _ = {}
    
    for index , value in enumerate(__):
        try:
            _ = float(value.get("BaiFenBi","").split("%")[0])
            if  _ > 50:result.append(f'{value.get("companyName")}|{value.get("BaiFenBi")}|{from_company}')
        except Exception as e:
            pass
    return result

@task_wrap
def get_company_link( target, page_text:str , base_url ="https://data.chinaz.com/" ):
    """ deal with https://data.chinaz.com/company/t0-p0-c0-i0-d0-s-{$company} """
    company_link = [ {"company":target+"".join(i.xpath("text()").extract()) , "link": urljoin( base_url ,   i.xpath("@href").extract()[0]) } for i in  Selector(page_text).xpath("//html/body/div[2]/div[2]/div/ul/li/a") ]
    return company_link

def get_paging_link(response , base_url = "https://data.chinaz.com/"):
    try:
        page_link =  [ urljoin( base_url,i) for i in  list(set(Selector(response.text).xpath("//html/body/div[2]/div[2]/div/div/ul/li/a[contains(@href,'com')]/@href").extract() ))] 
    except Exception as e:
        logger.info("Nope paging")
        return 
    logger.info(repr(page_link))
    return page_link

@task_wrap
def get_domain(response , base_url = "https://data.chinaz.com/"):
    domains = list(set(Selector(response).xpath("//html/body/div[3]/div[4]/div[6]/table/tbody/tr/td/a[contains(@href,'com')]/text()").extract() ))
    return domains

@task_wrap
def comapany_search(target):
    """ companyName search main """
    domains = []
    parse_url = urlparse(f"https://data.chinaz.com/company/t0-p0-c0-i0-d0-s-{quote(target)}")
    base_url = f"{parse_url.scheme}://{parse_url.netloc}/"
    response = requests.get(parse_url.geturl() , headers = headers)
    company_link = get_company_link(target = target , base_url = base_url , page_text = response.text)
    page_link = get_paging_link(response=response)
    # if page_link:
    #     for link in page_link : company_link.extend(get_company_link(page_text = requests.get(link.get('link') , headers = headers).text , target = link.get('company')))
    
    logger.success(f"page_link: {str(len(company_link))}")
    logger.debug(company_link )
    

    for link in company_link:
        _req2 = requests.get(link.get('link') , headers = headers)
        domains.extend(get_domain(response =_req2.text ) )
        if "对外投资" in _req2.text:_FenZhiJiGou.extend(get_FenZiJiGou(Selector( _req2.text )))
    logger.success(f"company len: {str(len(domains))}")
    # print(*domains , sep="\n")
    return domains

@task_wrap
def get_company_detail(target):
    """ domain search main """
    _domains = []
    link_list = []
    _ = requests.get(f"https://icp.chinaz.com/{target.strip()}" , headers = headers)
    sel = Selector(_.text)
    links = [ urljoin( f"http://{target.strip()}" , i.xpath('@href').extract()[0]) for i in sel.xpath('//html/body/div/div/div/div/ul/li/p/a') if not i.xpath('@href').extract()[0].startswith('javascript') and i.xpath('@href').extract()[0] != ''  ] 
    for link in links:
        if link.startswith("http://data" ):
            _sel = Selector(requests.get(link , headers = headers).text)
            main_company_link = [ urljoin(f"https://data.chinaz.com" , i) for i in  _sel.xpath('//body/div/div/div/ul/li/a/@href').extract() ] 
            main_company = _sel.xpath("//body/div/div/div/ul/li/a/span/text()")[0].extract()
            for x in main_company_link:
                _ = requests.get(x , headers = headers).text
                if "对外投资" in _:_FenZhiJiGou.extend(get_FenZiJiGou(Selector( _ )))
                for q in  Selector( _ ).xpath("//body/div/div/div/table/tbody/tr/td/text()").extract():
                    if q.startswith('www'):
                        _domains.append( ".".join(domain_extract(q)[1:]))
                # _domains.extend([ ".".join(domain_extract(q)[1:]) for q in  Selector(requests.get(x , headers = headers).text ).xpath("//body/div/div/div/table/tbody/tr/td/text()").extract()  ])  
            link_list.extend([ main_company+"".join(i) for i in _sel.xpath('//body/div/div/div/ul/li/a/text()').extract() ] )
            link_list.append(main_company)
    logger.debug(link_list)
    logger.info(f"company len: {str(len(main_company))}")
    for index , value  in enumerate(_domains):
        if "," in  value:
            _domains.extend(_domains.pop(index).split(","))
    return _domains

if __name__ == "__main__":
    logger = getLogger()
    if len(argv) < 2 :
        raise Exception(f"\nusage:\npython3 {argv[0]} domain\npython3 {argv[0]} companyName\npython3 {argv[0]} domain companyName\nor loop sub company query\npython3 {argv[0]} domain companyName -l ")
    targets = argv[1:]
    if '-d' in argv[1:]:
        import logging
        logging.getLogger().setLevel(logging.DEBUG)
        targets.remove('-d')
    if '-l' in argv[1:]:
        loop = True
        targets.remove('-l')
    else:
        loop = False
    logger.info(targets)
    for target in targets:
        if '.' in target:print(*get_company_detail(target) , sep = "\n")
        else:print(*comapany_search(target) , sep ="\n")
    sys.stderr.write("分支机构 \n")
    for i in _FenZhiJiGou:sys.stderr.write(str(i)+"\n")
    if loop:
        for i in _FenZhiJiGou:
            logger.info(i)
            print(*comapany_search(i.split('|')[0]) , sep ="\n")