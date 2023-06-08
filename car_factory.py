from engine1.capulet_engine import CapuletEngine
from engine1.sternman_engine import SternmanEngine
from engine1.willoughby_engine import WilloughbyEngine
from battery_types.nubbin_battery import NubbinBattery
from battery_types.spindler_battery import SpindlerBattery
from tyres_types.carrigan_tyres import CarriganTyres
from tyres_types.octoprime_tyres import OctoprimeTyres
from car import Car

from datetime import date
from enum import Enum


class TyreMapping(Enum):
    CARRIGAN = 1
    OCTOPRIME = 2


class CarFactory:
    @staticmethod
    def create_calliope(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        tyre_wear_array: list[float],
        tyre_map: TyreMapping,
    ) -> Car:
        engine = CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )
        battery = SpindlerBattery(
            last_service_date=last_service_date, current_date=current_date
        )
        if tyre_map == 1:
            tyre = CarriganTyres(tyre_wear_array)
        elif tyre_map == 2:
            tyre = OctoprimeTyres(tyre_wear_array)
        else:
            tyre = CarriganTyres([0, 0, 0, 0])
        return Car(engine, battery, tyre)

    @staticmethod
    def create_glissade(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        tyre_wear_array: list[float],
        tyre_map: int,
    ) -> Car:
        engine = WilloughbyEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )
        battery = SpindlerBattery(
            last_service_date=last_service_date, current_date=current_date
        )
        if tyre_map == 1:
            tyre = CarriganTyres(tyre_wear_array)
        elif tyre_map == 2:
            tyre = OctoprimeTyres(tyre_wear_array)
        else:
            tyre = CarriganTyres([0, 0, 0, 0])
        return Car(engine, battery, tyre)

    @staticmethod
    def create_palindrome(
        current_date: date,
        last_service_date: date,
        warning_light_on: bool,
        tyre_wear_array: list[float],
        tyre_map: int,
    ) -> Car:
        engine = SternmanEngine(warning_light_is_on=warning_light_on)
        battery = SpindlerBattery(
            last_service_date=last_service_date, current_date=current_date
        )
        if tyre_map == 1:
            tyre = CarriganTyres(tyre_wear_array)
        elif tyre_map == 2:
            tyre = OctoprimeTyres(tyre_wear_array)
        else:
            tyre = CarriganTyres([0, 0, 0, 0])

        return Car(engine, battery, tyre)

    def create_rorschach(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        tyre_wear_array: list[float],
        tyre_map: int,
    ) -> Car:
        engine = WilloughbyEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )
        battery = NubbinBattery(
            last_service_date=last_service_date, current_date=current_date
        )
        if tyre_map == 1:
            tyre = CarriganTyres(tyre_wear_array)
        elif tyre_map == 2:
            tyre = OctoprimeTyres(tyre_wear_array)
        else:
            tyre = CarriganTyres([0, 0, 0, 0])

        return Car(engine, battery, tyre)

    @staticmethod
    def create_thovex(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        tyre_wear_array: list[float],
        tyre_map: int,
    ) -> Car:
        engine = CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )
        battery = NubbinBattery(
            last_service_date=last_service_date, current_date=current_date
        )
        if tyre_map == 1:
            tyre = CarriganTyres(tyre_wear_array)
        elif tyre_map == 2:
            tyre = OctoprimeTyres(tyre_wear_array)
        else:
            tyre = CarriganTyres([0, 0, 0, 0])
        return Car(engine, battery, tyre)
