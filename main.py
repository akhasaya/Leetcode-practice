def segments(message):
    if len(message) <= 160:
        return message

    print(message)
    print("length is")
    print(len(message))
    # no_seg = len(message) / 155;

    # split_messages = []
    # for i in range(no_seg):
    #     split_message = message[0+i*155:(i+1)*155 + 1]
    #     split_message += "("+str(i)+"/"+str(no_seg)
    #     split_messages.append(split_message)

    # return split_messages

    # #split_message= [message[0+i:i+155] for i in range(0,len(message),155)]


if __name__ == '__main__':
    message = raw_input()

    result = segments(message)

    print(result)
