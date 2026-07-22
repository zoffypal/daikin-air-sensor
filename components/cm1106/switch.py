import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import switch,uart
from esphome.const import CONF_UART_ID
DEPENDENCIES=["uart"]
ns=cg.esphome_ns.namespace("cm1106")
CM1106CalibrateSwitch=ns.class_("CM1106CalibrateSwitch",switch.Switch)
CONFIG_SCHEMA=switch.switch_schema(CM1106CalibrateSwitch).extend({cv.Required(CONF_UART_ID):cv.use_id(uart.UARTComponent)})
async def to_code(config):
 var=await switch.new_switch(config);cg.add(var.set_uart_parent(await cg.get_variable(config[CONF_UART_ID])))
