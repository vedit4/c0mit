def parse(data:str):
    list_ = data.split(sep=":")
    items = ([int(x) for x in list_])
    return items

def main():
    ip =  "192:168:0:1"
    parsed = parse(ip)

    if 1 in parsed:
        print(parsed)
    elif 2 not in parsed:
        print(";".join([str(x) for x in parsed])) # list comprehention
    else:
        print(parsed[-1])
if __name__ == "__main__":
    main()
