from django.http import HttpResponse


#定义异常的中间件 exception无法处理404的错误
class MyException():
    def process_exception(request, response, exception):
        return HttpResponse(exception)
