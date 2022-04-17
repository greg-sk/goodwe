#!/bin/sh

date
echo
./script2.py | grep -E 'ppv:|total_inverter_power:|^active_power:|backup_ptotal:|load_ptotal:|e_day:|e_day_exp:|e_day_imp:|e_load_day:|e_bat_charge_day:|e_bat_discharge_day:|house_consumption:|battery_soc:|^active_power_total:|meter_active_power_total:|pbattery1:|battery_mode_label:'
