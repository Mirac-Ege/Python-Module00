def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def counter(count):
        if days < count:
            print("Harvest time!")
            return
        print("Day",count)
        counter(count + 1)
    counter(1)
