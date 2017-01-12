import collections
import heapq
class Music_Player(object):
    def __init__(self, song_list): #input is tuple (band, song name)
        self.band_songMap={}  # band name to set()
        self.band_pq_map={}
        for ite in song_list:
            if ite[0] not in self.band_songMap:
                self.band_songMap[ite[0]]=set(ite[1])
                self.band_pq_map[ite[0]]=[(0,ite[1])]
            else:
                self.band_songMap[ite[0]].add(ite[1])
                heapq.heappush(self.band_pq_map[ite[0]],(0, ite[1]))
    def play(self,band_name, song_name):
        if band_name in self.band_songMap and song_name in self.band_songMap[band_name]:
            for ite in self.band_pq_map[band_name]:
                if ite[1]==song_name:
                    item=ite
                    self.band_pq_map[band_name].remove(ite)
                    self.band_pq_map[band_name].append((item[0]-1,item[1]))
                    heapq.heapify(self.band_pq_map[band_name])
        else:
            print 'no band name or the song is not in this band'

    def topSong(self,band_name):
        return min(self.band_pq_map[band_name])