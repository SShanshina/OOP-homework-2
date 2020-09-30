class Track:

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f'{self.name} - {self.duration} минуты'

    def __lt__(self, other):
        return self.duration < other.duration


track_1 = Track('FAKE LOVE', 4)
track_2 = Track('The Truth Untold', 4)
track_3 = Track('Anpanman', 4)
track_4 = Track('Interlude: Shadow', 4)
track_5 = Track('Black Swan', 3)
track_6 = Track('ON', 4)


class Album:

    def __init__(self, group, name, tracks):
        self.group = group
        self.name = name
        self.tracks = tracks

    def get_tracks(self):
        track_list = ''
        for track in self.tracks:
            track_list += f'{str(track)}\n\t\t'
        return track_list

    def __str__(self):
        return f'Group name: {self.group}\nAlbum name: {self.name}\nTracks:\n\t\t{self.get_tracks()}'

    def add_track(self):
        track_name = input('Введите название трека: ')
        track_duration = int(input('Введите длительность трека: '))
        track_7 = Track(track_name, track_duration)
        self.tracks.append(track_7)
        return f'Трек {track_7.name} был успешно добавлен в альбом {self.name}, его длительность составляет {track_7.duration} минуты'

    def get_duration(self):
        duration_list = []
        for track in self.tracks:
            duration_list.append(track.duration)
        return f'Длительность альбома {self.name} составляет {sum(duration_list)} минут'


album_1 = Album('BTS', 'Love Yourself: Tear', [track_1, track_2, track_3])
album_2 = Album('BTS', 'Map Of The Soul: 7', [track_4, track_5, track_6])


print(album_1)
print(track_1)
print(track_5)
print(track_1 > track_5)