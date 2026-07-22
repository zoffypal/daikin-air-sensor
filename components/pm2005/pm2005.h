#pragma once
#include "esphome/components/i2c/i2c.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/core/component.h"
#include "esphome/core/log.h"
namespace esphome::pm2005 {
class PM2005Sensor:public PollingComponent,public sensor::Sensor,public i2c::I2CDevice { public:void update() override {uint8_t d[12]{};if(read(d, sizeof(d)) != i2c::ERROR_OK){ESP_LOGW("pm2005","I2C read failed");return;}if(d[3]!=0x80){ESP_LOGD("pm2005","Measurement not ready: 0x%02X",d[3]);return;}publish_state((uint16_t(d[6])<<8)|d[7]);}};
} // namespace esphome::pm2005
