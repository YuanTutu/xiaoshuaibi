# #使用js2py调用js函数的测试
# import js2py
# f = js2py.eval_js('function f(x) {return x + x}')
# print(f(2))
# print(f(f))

# #使用pyv8，但是pyv8就是装不上去我！@#￥%……&*
# import PyV8
# with PyV8.JSContext() as ctxt:
#     ctxt.eval("""
#                 var_ex1 = 1;
#                 var_ex2 = 1.0;
#                 var_ex3 = "test";
#                 var_ex4 = true;
#             """)
#     vars = ctxt.locals
#     var_ex1 = vars.var_ex1
#     print(var_ex1)

#使用PyExecJS
import execjs
print(execjs.eval("'red yellow blue'.split(' ')"))

ctx = execjs.compile("""
    function add(x,y){
        return x+y;
        }
    """)
A=ctx.call("add",1,2)
print(A)