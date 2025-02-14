# try:
#     print(x)
# except NameError:
#     print("Variable x is not defined")
# except:
#     print("Something else went wrong")
#
#
# #else only execute when there is no error.
# try:
#     print(x)
# except:
#     print("Something else went wrong")
# else:
#     print("else part.")
#
# #finally execute each time
# try:
#     print("hello")
# except:
#     print("something wrong")
# finally:
#     print("here the finally call.")

# try:
#     f=open("hey.txt","r")
#     data=f.read()
#     print(data)
# # except FileNotFoundError as e:
# #     print(e)
# except IOError as e:
#     print(e)
# except:
#     print("something wrong")
# finally:
#     print("end")


# try:
#     f=open("hey.txt","r")
#     try:
#         data=f.read()
#         print(data)
#     except FileNotFoundError as e:
#         print(e)
#     except ValueError as x:
#         print(x)
#     except IOError as e:
#         print(e)
#     except:
#         print("Uknown error")
#     finally:
#         f.close()
# except:
#     print("failed")
# finally:
#     print("all done.")


# try:
#     f=open("hey.txt",'r')
#     data=f.read()
#     print(data)
# except (IOError,ValueError) as e:
#     print(e)
# finally:
#     print("end")
#
# try:
#     x=7
#     list1=[]
#     list1.remove(x)
#
# except ValueError as e:
#     print(e)
# except:
#     print("another error")
# finally:
#     print("finally")
#


# class MyException(Exception):
#     pass
#
# raise MyException("error")


# class BadNumberException(Exception):
#     pass
#
# def mynum(a,b):
#     if a==3:
#         raise BadNumberException(" i don't like 3")
#     return a+b
#
#
# mynum(3,2)


try:
    with open("hey.txt","r") as f:
        try:
            data=f.read()
            print(data)
        except IOError as e:
            print(e)
        except:
            print("something else error")
        else:
            print("else part")
        finally:
            f.close()
            print(".....end")
except:
    print("outside except")
finally:
    print("all done")