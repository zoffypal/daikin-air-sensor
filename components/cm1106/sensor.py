import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, uart
from esphome.const import CONF_UART_ID, DEVICE_CLASS_CARBON_DIOXIDE, STATE_CLASS_MEASUREMENT, UNIT_PARTS_PER_MILLION
DEPENDENCIES=["uart"]
ns=cg.esphome_ns.namespace("cm1106")
CM1106Sensor=ns.class_("CM1106Sensor",cg.PollingComponent,sensor.Sensor)
CONFIG_SCHEMA=sensor.sensor_schema(CM1106Sensor,unit_of_measurement=UNIT_PARTS_PER_MILLION,accuracy_decimals=0,device_class=DEVICE_CLASS_CARBON_DIOXIDE,state_class=STATE_CLASS_MEASUREMENT).extend(cv.polling_component_schema("10s")).extend({cv.Required(CONF_UART_ID):cv.use_id(uart.UARTComponent)})
async def to_code(config):
 var=await sensor.new_sensor(config);await cg.register_component(var,config);cg.add(var.set_uart_parent(await cg.get_variable(config[CONF_UART_ID])))
