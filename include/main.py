class Manager:
    def __call__(self, tasks):
        self.IsStopped = False
        # Основной цикл
        while not self.IsStopped:
            # Основная функция
            self.main(tasks)

            if self.IsStopped:
                break

            value = input("Введите 'yes' или 'y', чтобы повторить программу, а для выхода нажмите Enter: ")
            if value != 'y' and value != 'yes':
                break

        print("Завершение программы")

    @staticmethod
    def GetValueByType(value, type_values):
        count_types=len(type_values)
        if count_types==0 or len(value)==0:
            return None

        # извлекаем из массива приоритетный тип, если указано несколько 
        #   {str,float,...} -> None (любое значение текст или число)
        ##   {float,int} -> float (любое число) исправить!!!!
        #   {int} -> only int (только целое)
        #   {str} -> only str (только текст)
        #   {float} -> only float (только вещественное)
        type_main = None
        type_combo = False
        if count_types==1:
            for item in type_values:
                type_main=item
        elif str not in type_values and float in type_values and int in type_values:
            type_main = float
            type_combo = True

        # проверяем
        if type_main==None:
            type_main=str
        elif type_main==str:
            try:
                float(value)
                return None
            except ValueError:
                if value.isnumeric():
                    return None
        elif type_main == float:
            if not type_combo:
                if value[0]=='-':
                    if value[1:len(value)].isnumeric():
                        return None
                else:
                    if value.isnumeric():
                        return None
        elif type_main == int:
            if value[0]=='-':
                if not value[1:len(value)].isnumeric():
                    return None
            else:
                if not value.isnumeric():
                    return None
        return type_main(value)

    def main(self, tuple):
        i=0
        while len(tuple)>i and not self.IsStopped:
            if not isinstance(tuple[i], dict):
                self.main(tuple[i])
                i+=1
                continue

            out = None
            value = None
            if "in" in tuple[i]:  
                if "out" in tuple[i]:
                    out = tuple[i]["out"]

                value = input(tuple[i]["in"])

                if "type" in tuple[i]:
                    try:
                        type_values=tuple[i]["type"]
                        if type(type_values)==type:
                            type_values={type_values}
                        
                        value=Manager.GetValueByType(value, type_values)
                        if value==None:
                            raise Exception()
                        
                    except:
                        print("Некорректное значение, ожидается {0}, пожалуйста повторите ввод!".format(tuple[i]["type"]))
                        continue
            elif "out" in tuple[i]:
                out = tuple[i]["out"]
                value = out

            try:
                if "def" in tuple[i]:
                    value = tuple[i]["def"](value,out)
                if value != None:
                    print(value)
            except Exception as e:
                if str(e)=="PositiveNumber":
                    i-=1
                    print("Некорректное значение, ожидается положительное число, пожалуйста повторите ввод!")
                elif str(e)=="NegativeNumber":
                    i-=1
                    print("Некорректное значение, ожидается отрицательное число, пожалуйста повторите ввод!")                    
                elif str(e)=="StrIsNotNumeric":
                    i-=1
                    print("Некорректное значение, ожидается число, пожалуйста повторите ввод!")
                elif str(e)=="StrFormatIsNotValid":
                    i-=1
                    print("Некорректный формат, пожалуйста смотрите пример и повторите ввод!")
                elif str(e)=="ValueOutOfRange":
                    i-=1
                    print("Значение вне диапазона, пожалуйста повторите ввод!") 
                elif str(e)=="ValueIsNull":
                    i-=1
                    print("Некорректное значение, оно не должно быть равно нулю, пожалуйста повторите ввод!")
                elif str(e)=="Repeat":
                    i-=1                    
                elif str(e)=="ProgramStop":
                    self.IsStopped=True                
                else:
                    print("Ошибка в конфигурации: "+str(e))               
                continue
            finally:
                i+=1        