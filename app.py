#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-
# @Author  : lwx607353 2019/8/16 19:11
import json
import click
import pickle
from typing import Dict


@click.group()
def main():
    pass


@main.command()
@click.option('--in_filr', required=True)
@click.option('--out_file', required=True)
def transform_json_to_txt(in_file: str, out_file: str):
    out = open(out_file, 'w')
    for line in open(in_file):
        result = parse_song_line(line)
        if result:
            out.write(result.strip() + "\n")
    out.close()


def parse_song_line(in_line: str) -> str:
    data = json.loads(in_line)
    name = data['result']['name']
    tags = ",".join(data['result']['tags'])
    subscribed_count = data['result']['subscribedCount']
    if subscribed_count < 100:
        return ''
    playlist_id = data['result']['id']
    song_info = ''
    songs = data['result']['tracks']
    for song in songs:
        try:
            song_info += "\t" + ":::".join(
                [str(song['id']), song['name'], song['artists'][0]['name'], str(song['popularity'])])
        except Exception:
            continue

    return name + "##" + tags + "##" + str(playlist_id) + "##" + str(subscribed_count) + song_info


@main.command()
@click.option('--in_filr', required=True)
@click.option('--out_file', required=True)
def create_surprise_data_from_txt(in_file: str, out_file: str):
    out = open(out_file, 'w')
    for line in open(in_file):
        result = parse_playlist_line(line)
        if result:
            out.write(result.strip() + "\n")
    out.close()


def parse_playlist_line(in_line: str) -> [str, bool]:
    try:
        contents = in_line.strip().split("\t")
        name, tags, playlist_id, subscribed_count = contents[0].split("##")
        songs_info = map(lambda x: playlist_id + "," + parse_song_info(x), contents[1:])
        songs_info = filter(is_null, songs_info)
        return "\n".join(songs_info)
    except Exception as ex:
        print(ex)
        return False


def is_null(s: str) -> bool:
    return len(s.split(",")) > 2


def parse_song_info(song_info: str) -> str:
    try:
        song_id, name, artist, popularity = song_info.split(":::")
        return ",".join([song_id, "1.0", '1300000'])
    except Exception as ex:
        print(ex)
        return ""


@main.command()
@click.option('--in_filr', required=True)
@click.option('--out_playlist', required=True)
@click.option('--out_song', required=True)
def save_playlist(in_file: str, out_playlist: str, out_song: str):
    playlist_dic = {}
    song_dic = {}
    for line in open(in_file):
        parse_playlist_get_info(line, playlist_dic, song_dic)
    pickle.dump(playlist_dic, open(out_playlist, "wb"))
    pickle.dump(song_dic, open(out_song, "wb"))


def parse_playlist_get_info(in_line: str, playlist_dic: Dict, song_dic: Dict):
    contents = in_line.strip().split("\t")
    name, tags, playlist_id, subscribed_count = contents[0].split("##")
    playlist_dic[playlist_id] = name
    for song in contents[1:]:
        try:
            song_id, song_name, artist, popularity = song.split(":::")
            song_dic[song_id] = song_name + "\t" + artist
        except Exception:
            print("song format error")
            print(song + "\n")
