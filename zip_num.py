import sys

num_li_1 = [1,3,5,7,8]
num_li_2 = [2,4,6]

def zus_num(num_li_1,num_li_2):
    for num1,num2 in zip(num_li_1,num_li_2):
        while num2 > 15:
            if num2%2 == 0:
                num2 += 2
                num_li_2.append(num2)
        u_name = num1 + num2
        return u_name

def main():
    print(zus_num(num_li_1,num_li_2))

if __name__ == "__main__":
    main()