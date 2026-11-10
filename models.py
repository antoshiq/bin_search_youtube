from asyncio.sslproto import _create_transport_context


class video:
    def __init__(self, title, link, channel, channel_id, view_count, like_count, comment_count):
        self.title = title
        self.link = link
        self.channel = channel
        self.channel_id = channel_id
        self.view_count = view_count
        self.like_count = like_count
        self.comment_count = comment_count


# "video_id","title","channel_name","channel_id","view_count","like_count","comment_count","published_date","thumbnail"

class MyHashMap:
    MAX_LOAD_FACTOR = 0.75

    def __init__(self, capacity: int = 8):

        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]


    def _index(self, key = None):


        return hash(key) % self.capacity


    def load_factor(self):


        return self.size / self.capacity


    def _resize(self):

        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]

        for bucket in old_buckets:
            for key, value in bucket:

                index = self._index(key)
                self.buckets[index].append((key, value))

    def put(self, key, value):

        index = self._index(key)
        bucket = self.buckets[index]

        for i in range(len(bucket)):
            if key == bucket[i][0]:
                bucket[i] = (key, value)

                return

        if (self.size + 1) / self.capacity > self.MAX_LOAD_FACTOR:
            self._resize()
            index = self._index(key)

        self.buckets[index].append((key, value))
        self.size += 1


    def get(self, key):

        index = self._index(key)
        bucket = self.buckets[index]

        for cont_key, cont_value in bucket:
            if cont_key == key:
                return cont_value

        return None


    def contains(self, key):

        index = self._index(key)
        bucket = self.buckets[index]

        for cont_key, cont_value in bucket:
            if cont_key == key:

                return True

        return False


    def remove(self, key):

        index = self._index(key)
        bucket = self.buckets[index]

        for i in range(len(bucket)):
            if key == bucket[i][0]:
                bucket.pop(i)
                self.size -= 1

                return True

        return False


    def __len__(self):

        return self.size
