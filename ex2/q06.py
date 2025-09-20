class SkipIterator:

    def __init__(self):
        self.content_list = []

    def skip_iterator(self, content, skip):
        for item in content:
            if (content.index(item) + 1) % skip == 0:
                self.content_list.append(item)
        return self.content_list

skipper = SkipIterator()

natural_numbers = [i for i in range(1,50)]
for num in skipper.skip_iterator(natural_numbers, 5):
    print(num, end=",")
print(end="\n\n")