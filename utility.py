from requests import get,post,patch,delete
from time import time
from time import sleep
import csv
from functools import wraps


token_url="https://captivateprimestage1.adobe.com/"
#token_url="https://captivateprimeeu.adobe.com/"
#token_url="https://captivateprime.adobe.com/"
#token_url="https://captivateprimeqe.adobe.com/"
base_url="https://captivateprimestage1.adobe.com/primeapi/v2/"
#base_url="https://captivateprime.adobe.com/primeapi/v2/"
#base_url="https://captivateprimeeu.adobe.com/primeapi/v2/"
#base_url="https://captivateprimeqe.adobe.com/primeapi/v2/"

#bapan1690814+9090@gmail.com.
status_code=0
csv_writer=None
#credentials
cred = {"client_id": "769e9ae8-ffc9-4477-b5f0-01acdbbc7b07",
        "client_secret": "d8d31b03-b19f-47ee-9664-844251e46a20","refresh_token":"086c2a8de0e73584e6ec3951bf48a030"}

#data parameter
data = {"page[offset]":'0',"page[limit]":'10',"sort":"name"}
f=None


def set_token_url(url):
    global token_url
    token_url=url


def Env_init(clientid,clientsecret,refreshtoken):
    global cred
    cred["client_id"]=clientid
    cred["client_secret"]=clientsecret
    cred["refresh_token"]=refreshtoken


#Generate Access Token
def get_New_Token(base_url,cred):
    header = {"Content-type":"application/x-www-form-urlencoded"}
    final_url =base_url+"oauth/token/refresh"
    try:
        response=post(final_url,params=cred,headers=header)
        data_json=response.json()
        print(data_json)
        return data_json
    except:
        print("Unable to generate the access token")
        pass
        return ""


# get request decorator
def get_request(func):
    global cred
    global l
    global data
    global base_url
    global token_url
    def wrapper(*args):
        url=base_url+str(args[0])
        Access_Token=get_New_Token(token_url,cred)
        hdr={"Authorization":"oauth "+Access_Token["access_token"]}
        print(url)
        print(data)
        res=get(url,params=data,headers=hdr)
        return func(args[0],res.json(),res.status_code)
    return wrapper



#get data
def get_data():
    return data



# patch request decorator
def patch_request_payload(func):
    global cred
    global l
    global data
    global base_url
    global token_url
    @wraps(func)
    def wrapper(*args):
        str1=base_url+str(args[0])
        print(str1)
        Access_Token = get_New_Token(token_url,cred)
        hdr = {"Authorization": "oauth " + str(Access_Token["access_token"]),"Content-type": "application/vnd.api+json","Accept": "application/vnd.api+json"}
        res = patch(str1,params=data,headers=hdr,data=args[1])
        print("Showing patch data")
        print(res.json())
        return func(args[0],args[1],res.json(),res.status_code)
    return wrapper




# #Pagination test for the endpoint. 
# def pagination_test(endpoint_string,data_per_page,total_record):
#     test=False
#     has_next_fail=False
#     data=get_data()
#     data["page[limit]"]=str(data_per_page)
#     counter=0
#     record_found=0
#     while not has_next_fail:
#         response=get_badges(endpoint_string)
#         if len(response["data"])==data_per_page:
#             counter=counter+1
#             data["page[offset]"]=str(data_per_page*counter)
#             record_found=record_found+data_per_page
#         elif len(response["data"])<data_per_page and len(response["data"])!=0:
#             counter=counter+1
#             record_found=record_found+len(response["data"])
#             if record_found<total_record:
#                 print("Pagination Fail")
#                 print("page number {}".format(counter))
#                 has_next_fail=True
#             elif record_found==total_record:
#                 print("Pagination is fine with badge")
#                 data["page[offset]"]=data_per_page*counter
#         elif len(response["data"])>data_per_page:
#             counter=counter+1
#             print("pagination fail")
#             print("page number {}".format(counter))
#             print("Records obtained {}".format(len(response["data"])))
#             test=False
#             has_next_fail=True
#         elif len(response["data"])==0:
#             if record_found==0:
#                 print("Blank response obtained")
#                 has_next_fail=True
#                 test=False
#             elif record_found<total_record:
#                 test=False
#                 has_next_fail=True
#             else:
#                 if record_found==total_record:
#                     test=True
#                     has_next_fail=True

#     return test


#Pagination test for the endpoint.
# def pagination_test_cursor(endpoint_string,data_per_page,total_record):
#     test=False
#     has_next_fail=False
#     data=get_data()
#     data["page[limit]"]=str(data_per_page)
#     data["page[cursor]"]=''
#     try:
#         del data["page[offset]"]
#     except KeyError as e:
#         print("Offset field is deleted")
#     counter=0
#     record_found=0
#     while not has_next_fail:
#         response=get_lo(endpoint_string)
#         if len(response["data"]) == data_per_page:
#             counter = counter + 1
#             data["page[cursor]"]=response["links"]["next"].split('&')[3].split('=')[1]
#             record_found = record_found + data_per_page
#         elif len(response["data"])<data_per_page and len(response["data"])!= 0:
#             counter = counter + 1
#             record_found=record_found + len(response["data"])
#             if record_found < total_record:
#                 print("Pagination Fail")
#                 print("page number {}".format(counter))
#                 has_next_fail = True
#             elif record_found == total_record:
#                 print("Pagination is fine with badge")
#                 data["page[cursor]"]=response["links"]["next"].split('&')[3].split('=')[1]
#         elif len(response["data"])>data_per_page:
#             counter = counter + 1
#             print("pagination fail")
#             print("page number {}".format(counter))
#             print("Records obtained {}".format(len(response["data"])))
#             test = False
#             has_next_fail = True
#         elif len(response["data"]) == 0:
#             if record_found == 0:
#                 print("Blank response obtained")
#                 has_next_fail = True
#                 test = False
#             elif record_found < total_record:
#                 test = False
#                 has_next_fail = True
#             else:
#                 if record_found==total_record:
#                     test = True
#                     has_next_fail = True

#     return test


# # get request with include parameter.
# def  get_request_include(func):
#     global cred
#     global data
#     def wrapper(*args):
#         url="https://captivateprime.adobe.com/primeapi/v2/"+str(args[0])
#         Access_Token=get_New_Token("https://captivateprimeqe.adobe.com/",cred)
#         hdr={"Authorization":"oauth "+Access_Token["access_token"]}
#         data["include"]=args[1]
#         data["page[limit]"]=str(1)
#         res=get(url,params=data,headers=hdr)
#         if res.status_code==400:
#             raise  BadRequestException("Bad request Exception")
#         elif res.status_code==401:
#             raise  UnAuthorizedException("Unauthorized Exception")
#         elif res.status_code==500:
#             raise  InternalServerError("Internal Server Error")
#         elif res.status_code==503:
#             raise  BusyServer("Server Under Maintainence")
#         return func(args[0],args[1],args[2])
#     return wrapper


def Auto_init(filename):
    global f
    global csv_writer
    f=open(filename,"w")
    csv_writer=csv.DictWriter(f,fieldnames=['TestCase','Verdict'])
    csv_writer.writeheader()
    return


def Report_generate(func):
    def wrapper(*args):
        global  csv_writer
        test=func(*args)
        csv_writer.writerow({'TestCase':args[0],'Verdict':str(test)})
    return wrapper

def Auto_close():
    global f
    f.close()
    return


def  post_request(func):
    global cred
    global l
    global data
    global base_url
    global token_url
    def wrapper(*args):
        url=base_url+str(args[0])
        Access_Token=get_New_Token(token_url,cred)
        hdr={"Authorization":"oauth "+Access_Token["access_token"]}
        print(url)
        print(args[1])
        res=post(url,params=args[1],headers=hdr)
        return func(args[0],args[1],res.json(),res.status_code)
    return wrapper


#post a payload using this decorator.
#func is the function object.
#The post method carries payload with it.
#args[0] is the endpoint string.
#args[1] is the payload object.json body.
#args[2] is the post method response object.
#args[3] is the status code of the response.

def post_request_payload(func):
    global cred
    global l
    global data
    global base_url
    global token_url
    @wraps(func)
    def wrapper(*args):
        str1=base_url+str(args[0])
        print(str1)
        Access_Token = get_New_Token(token_url,cred)
        hdr = {"Authorization": "oauth " + str(Access_Token["access_token"]),"Content-type": "application/vnd.api+json","Accept": "application/vnd.api+json"}
        res = post(str1,params=data,headers=hdr,data=args[1])
        print(res.json())
        return func(args[0],args[1],res.json(),res.status_code)
    return wrapper


def delete_request_payload(func):
    global cred
    global l
    global data
    global base_url
    global token_url
    @wraps(func)
    def wrapper(*args):
        str1=base_url+str(args[0])
        Access_Token = get_New_Token(token_url,cred)
        hdr = {"Authorization": "oauth " + str(Access_Token["access_token"]),"Content-type": "application/vnd.api+json","Accept": "application/vnd.api+json"}
        res = delete(str1,headers=hdr,data=args[1])
        print(res)
        return func(args[0],args[1],res.json(),res.status_code)
    return wrapper


def delete_request_parameter(func):
    global cred
    global l
    global data
    global base_url
    global token_url
    @wraps(func)
    def wrapper(*args):
        str1=base_url+str(args[0])
        Access_Token = get_New_Token(token_url,cred)
        hdr = {"Authorization": "oauth " + str(Access_Token["access_token"]),"Content-type": "application/vnd.api+json","Accept": "application/vnd.api+json"}
        res = delete(str1,headers=hdr)
        print(res)
        return func(args[0],res.status_code)
    return wrapper






































   

   


   
   

   

   

   

   
   
   
   
   




   




    
      
