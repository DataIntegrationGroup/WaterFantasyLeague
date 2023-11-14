# ===============================================================================
# Copyright 2023 ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================
from sqlalchemy import (
    DateTime,
    Column,
    Boolean,
    String,
    ForeignKey,
    Float,
    TIMESTAMP,
    func,
)

from api.database import Slugged, Base


class Game(Base, Slugged):
    start = Column(DateTime, nullable=False)
    active = Column(Boolean, default=False)


class Match(Base, Slugged):
    roster_a = Column(String(128), ForeignKey("roster.slug"))
    roster_b = Column(String(128), ForeignKey("roster.slug"))
    game = Column(String(128), ForeignKey("game.slug"))

    score_a = Column(Float, nullable=True)
    score_b = Column(Float, nullable=True)
    timestamp = Column(TIMESTAMP, nullable=True, default=func.now())


# ============= EOF =============================================
