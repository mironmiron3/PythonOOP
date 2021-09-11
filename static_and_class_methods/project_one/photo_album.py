from math import ceil

class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[]] * self.pages #ceil(self.pages/4)

    def add_photo(self, label: str):
        is_added = False
        for sublist in self.photos:
            if len(sublist) == 4:
                continue
            else:
                sublist.append(label)
                is_added = True
                return f"{label} photo added successfully on page {self.photos.index(sublist) + 1} slot {len(sublist)}"

        if not is_added:
            return "No more free slots"

    @classmethod
    def from_photos_count(cls,photos_count: int):
        return cls(ceil(photos_count/4))


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))


