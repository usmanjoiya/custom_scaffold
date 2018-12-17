import os, sys , re
from optparse import OptionParser
from pathlib import Path

PYTHON = 'python3'
parser = OptionParser()
parser.add_option("-f", "--form",
                  help="Make a form",
                  action="store_true",
                  dest="Form"
                  )
parser.add_option("-m", "--module",
                  help="Make a module",
                  action="store_true",
                  dest="Module"
                  )
options, arguments = parser.parse_args()

def demo_data():
    path = open("path.txt", "w")
    path.write('odoo-bin path\r\n')
    path.write('custom module path\r\n')
    path.write('custom scaffold path =/home/joey/Desktop/python_learn_by_dummies/venv/qwexer_scaffold\r\n')
    path.close()

def odoo_bin_path():
    with open("path.txt", "r") as path:
        data = path.readlines()
        mod_path = input("Enter the Path where your odoo-bin file present:  ")
        if os.path.exists(mod_path):
            os.chdir(mod_path)
            files = [f for f in os.listdir('.')]
            count = 0
            for f in files:
                if f == 'odoo-bin':
                    count = count + 1
            if count == 1:
                os.chdir(sys.path[0])
                data[0] = 'odoo-bin path =' + mod_path + '/odoo-bin' + '\r\n'
                with open('path.txt', 'w') as file:
                    print(os.getcwd())
                    file.writelines(data)
                    file.close()
                    path.close()
                    os.system("clear")
                    print("your odoo-bin path is \n", data[0])
                    return 1


            elif count > 1:
                os.system("clear")
                print("there are more then one odoo-bin file how is it possible")
                path.close()
                return 0

            else:
                os.system("clear")
                print("there are not any odoo-bin file here so again enter proper path")
                path.close()
                return 0

        else:
            os.system("clear")
            print('This path is not exist in your directories')
            path.close()
            return 0

def custum_module_path():
    with open("path.txt", "r") as path:
        data = path.readlines()
        mod_path = input("Enter the path of your Custom Module Path:  ")
        if os.path.exists(mod_path):
            data[1] = 'custom module path =' + mod_path + '\r\n'
            with open('path.txt', 'w') as file:
                file.writelines(data)
                file.close()
                path.close()
                os.system("clear")
                print("your custom module path is \n", data[1])
                return 1

        else:
            os.system("clear")
            print("You enter a wrong path its not exist")
            path.close()

def build_path_file():
    demo_data()
    val1 =0
    val2 = 0

    while val1 != 1:
        val1 =odoo_bin_path()

    while val2 != 1:
        val2 =custum_module_path()

def read_path():
    f = open("path.txt", "r")
    python_bin_path = f.readline()
    module_path = f.readline()

    print('', python_bin_path, module_path)

    f.close()

def make_scaffold():
    with open("path.txt", "r") as path:
        data = path.readlines()
        bin_path = data[0].split('=')[1]
        module_path = data[1].split('=')[1]
        scaffold_path = data[2].split('=')[1]

        bin_path = bin_path.replace('\n','')
        bin_path = bin_path.split('/')
        lent = len(bin_path)
        lan2 = lent -4
        i = 0
        path1 = ''
        while lan2 >= i:
            path1 = path1+'/'+bin_path[i+3]
            i = i+ 1

        module_path = module_path.replace('\n', '')
        module_path = module_path.split('/')
        lent = len(module_path)
        lan2 = lent - 4
        i = 0
        path2 = ''
        while lan2 >= i:
            path2 = path2+ module_path[i + 3]+ '/'
            i = i + 1


        scaffold_path = scaffold_path.replace('\n', '')
        scaffold_path = scaffold_path.split('/')
        lent = len(scaffold_path)
        lan2 = lent - 4
        i = 0
        path3 = ''
        while lan2 >= i:
            path3 = path3+ scaffold_path[i + 3]+ '/'
            i= i+1
        module_name = input("Enter you module name:  ")
        module_name = module_name.replace(' ','_')
        make_it_one = '.'+path1+" scaffold -t "+path3+' '+module_name+ ' '+path2
        path.close()
        home = str(Path.home())
        os.chdir(home)
        os.system(make_it_one)
        os.chdir(sys.path[0])
        return module_name

def manage_module():
    PATH = 'path.txt'
    if os.path.isfile(PATH):
        read_path()

        while 1:
            val =input("Are you ok with above path? (y/n)")
            if val =='Y' or val =="y":
                break

            elif val =='N' or val =="n" :

                val2 =input("Do you want to setup path (y/n)")
                if val2== "y" or val2== "Y":
                    odoo_bin_path()
                    custum_module_path()

                elif val2== "n" or val2== "N":
                    break
                else:
                    print("invalid key:  ", val2, " option is not avaliable")

            else:
                print("invalid key:  " ,val," option is not avaliable" )

    else:
        build_path_file()

    file_name = make_scaffold()
    return file_name

def models_form(file_name,form_):
    f = open("path.txt", "r")
    data = f.readlines()

    module_path = data[1].split('=')[1]
    module_path= module_path.replace('\n','')

    scaffold_path =data[2].split('=')[1]
    scaffold_path= scaffold_path.replace('\n','')

    f.close()

    scaffold_path= scaffold_path+'/'+'models/models.py.template'

    module_path= module_path+'/'+file_name+'/models'+'/'
    form_= form_+'.py'

    os.chdir(module_path)
    module_path= module_path+form_
    print(module_path)
    print(scaffold_path)

    with open(scaffold_path) as f:
        with open(module_path, "w") as f1:
            for line in f:
                f1.write(line)
        f1.close()
    f.close()

    print("""""OK""""")

    with open(module_path, "r") as path:
        data = path.readlines()
        form_= form_.replace('.py','')
        form_ = form_.capitalize()
        print(form_)
        print(form_)
        print(form_)
        print(form_)
        print(form_)
        print(form_)
        data[4] = "class "+form_.replace('_','')+"(models.Model):"
        form_ = '.'.join(form_.lower().split())
        # form_ = form_.replace('_',".")
        data[5] = "    _name= "+"'"+form_+"'"

        # with open(module_path, 'w') as file:
        #     file.writelines(data)
        #     file.close()
        #     path.close()
        print(data[4])
        print(data[5])


def manage_form(file_name):
    form_ = input('Enter the class name you want to Enter:   ')
    form_=form_.replace(' ','_')
    models_form(file_name,form_)

def main():
    if options.Module:
        file_name =manage_module()
        # file_name ='module_test'
        manage_form(file_name)


if __name__ == '__main__':
    main()