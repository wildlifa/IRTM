class FrequencyVector:

    def __init__(self):
        self.__frequency_list = []

    def generate_vector_from_list(self, my_list):
        self.__frequency_list = []
        counter = 0
        while counter < len(my_list):
            content = my_list[counter][0]
            frequency = 1
            for sub_counter in range(counter + 1, len(my_list)):
                next_content = my_list[sub_counter][0]
                if content == next_content:
                    frequency = frequency + 1
                else:
                    break
            item = (frequency, content)
            self.__frequency_list.append(item)
            counter = counter + frequency
        return self.__frequency_list
