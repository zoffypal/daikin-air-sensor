import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c,sensor
from esphome.const import DEVICE_CLASS_PM25,STATE_CLASS_MEASUREMENT,UNIT_MICROGRAMS_PER_CUBIC_METER
DEPENDENCIES=["i2c"]
ns=cg.esphome_ns.namespace("pm2005")
PM2005Sensor=ns.class_("PM2005Sensor",cg.PollingComponent,sensor.Sensor,i2c.I2CDevice)
CONFIG_SCHEMA=sensor.sensor_schema(PM2005Sensor,unit_of_measurement=UNIT_MICROGRAMS_PER_CUBIC_METER,accuracy_decimals=0,device_class=DEVICE_CLASS_PM25,state_class=STATE_CLASS_MEASUREMENT).extend(cv.polling_component_schema("1s")).extend(i2c.i2c_device_schema(0x28))
async def to_code(config):
 var=await sensor.new_sensor(config);await cg.register_component(var,config);await i2c.register_i2c_device(var,config)
