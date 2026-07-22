#pragma once
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/switch/switch.h"
#include "esphome/components/uart/uart.h"
#include "esphome/core/component.h"
#include "esphome/core/log.h"
namespace esphome::cm1106 {
class CM1106 { public: explicit CM1106(uart::UARTComponent *p):p_(p) {} int16_t read() { uint8_t c[]={0x11,0x01,0x01,0xED},r[8]{}; clear_(); p_->write_array(c,sizeof(c)); p_->flush(); if(!p_->read_array(r,sizeof(r))||r[0]!=0x16||r[1]!=0x05||r[2]!=0x01||r[7]!=crc_(r,sizeof(r))) return -1; return (r[3]<<8)|r[4]; } bool calibrate() { uint8_t c[]={0x11,0x03,0x03,0,0,0},r[4]{}; c[5]=crc_(c,sizeof(c)); clear_(); p_->write_array(c,sizeof(c)); p_->flush(); return p_->read_array(r,sizeof(r))&&r[0]==0x16&&r[1]==0x01&&r[2]==0x03&&r[3]==0xE6; } protected: uint8_t crc_(const uint8_t*d,size_t n) { uint8_t c=0; for(size_t i=0;i<n-1;i++)c-=d[i]; return c; } void clear_(){uint8_t discard; while (p_->available()) p_->read_byte(&discard);} uart::UARTComponent*p_; };
class CM1106Sensor:public PollingComponent,public sensor::Sensor { public:void set_uart_parent(uart::UARTComponent*p){dev_=new CM1106(p);} void update() override {auto v=dev_->read();if(v>=0)publish_state(v);} protected:CM1106*dev_{nullptr};};
class CM1106CalibrateSwitch:public switch_::Switch { public:void set_uart_parent(uart::UARTComponent*p){dev_=new CM1106(p);} protected:void write_state(bool state) override {if(state&&!dev_->calibrate())ESP_LOGW("cm1106","Calibration failed");publish_state(false);} CM1106*dev_{nullptr};};
} // namespace esphome::cm1106
