class FileHandler:
    def read_file(self):
        try:
            file=open("simple1.txt","r")
            data=file.read()
            print("Data Is:",data)
            file.close()
        except FileNotFoundError:
            print("Error: file not found")
        except PermissionError:
            print("Error: Permission Denied")
        except Exception as e:
            print(e)
        finally:
            print("Program Executed")
            
obj=FileHandler()
obj.read_file()