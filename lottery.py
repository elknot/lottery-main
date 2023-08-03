import sys
import random

def read_names(filename):
    with open(filename, 'r') as file:
        names = [line.strip() for line in file]
    return names

def pick_winners(names, num_winners):
    return random.sample(names, num_winners)

def output_winners(winners, output_file=None):
    if output_file:
        with open(output_file, 'w') as file:
            for winner in winners:
                file.write(winner + '\n')
    else:
        print("中奖者:")
        for winner in winners:
            print(winner)

def main():
    if len(sys.argv) < 4:
        print("用法: python3 lottery.py <名单文件> <中奖者个数> <输出方式（'console'或者'file'）> [输出文件]")
        sys.exit(1)

    filename = sys.argv[1]
    num_winners = int(sys.argv[2])
    output_mode = sys.argv[3]
    output_file = sys.argv[4] if output_mode == 'file' else None

    names = read_names(filename)

    if num_winners > len(names):
        print("中奖者数量不能超过名单数量！")
        sys.exit(1)

    winners = pick_winners(names, num_winners)
    output_winners(winners, output_file)

if __name__ == "__main__":
    main()
