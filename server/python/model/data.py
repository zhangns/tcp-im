"""
SCRP Data representation and validation.
"""

# Copyright (C) 2015 Zhang NS, Zifan Li, Zichao Li
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import re

from .error import *


class User:
    id_pattern = re.compile(r'^\w{1,16}$', re.A)
    # TODO: other patterns

    def __init__(self, id_: str, password: str, nickname: str, description:str,
                 sign_up_time: int, last_activity_time: int):
        if not User.id_pattern.match(id_):
            raise InvalidUserIdError()
        self.id_ = id_
        self.password = password
        self.nickname = nickname
        self.description = description
        self.sign_up_time = sign_up_time
        self.last_activity_time = last_activity_time


class RoomMessage:
    def __init__(self):
        pass


class Room:
    def __init__(self):
        pass


class PrivateMessage:
    def __init__(self):
        pass


class Friendship:
    def __init__(self):
        pass