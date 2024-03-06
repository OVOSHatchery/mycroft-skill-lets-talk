# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.
from ovos_workshop.intents import IntentBuilder
from ovos_workshop.skills import OVOSSkill

__author__ = 'chrison999'


class LetsTalkSkill(OVOSSkill):

    def initialize(self):
        good_morning_intent = IntentBuilder("GoodMorningIntent"). \
            require("GoodMorningKeyword").build()
        self.register_intent(good_morning_intent,
                             self.handle_good_morning_intent)

        good_afternoon_intent = IntentBuilder("GoodAfternoonIntent"). \
            require("GoodAfternoonKeyword").build()
        self.register_intent(good_afternoon_intent,
                             self.handle_good_afternoon_intent)

        good_evening_intent = IntentBuilder("GoodEveningIntent"). \
            require("GoodEveningKeyword").build()
        self.register_intent(good_evening_intent,
                             self.handle_good_evening_intent)

        good_night_intent = IntentBuilder("GoodNightIntent"). \
            require("GoodNightKeyword").build()
        self.register_intent(good_night_intent, self.handle_good_night_intent)

    def handle_good_morning_intent(self, message):
        self.speak_dialog("good.morning")

    def handle_good_afternoon_intent(self, message):
        self.speak_dialog("good.afternoon")

    def handle_good_evening_intent(self, message):
        self.speak_dialog("good.evening")

    def handle_good_night_intent(self, message):
        self.speak_dialog("good.night")
