#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Transmission(object):
    def __init__(self,distance=50000000,bandwidth=2000000000,light_speed=200000000):
        self.__distance =distance
        self.__bandwidth = bandwidth
        self.__light_speed = light_speed

    def __str__(self):
        distance ='distance: ' + str(round(self.__distance/1000,1)) + 'km'
        bandwidth ='bandwidth: ' + str(round(self.__bandwidth/1000000000,1)) +'Gbps'
        light_speed ='light_speed: ' + str(round(self.__light_speed/1000,1)) + 'km/s'
        print('Between host A and B:\n{}\n{}\n{}\n'.format(distance,bandwidth,light_speed))

    def max_bits(self,file_bits=0):
        propagation_time = self.__distance/self.__light_speed
        out_time = round(propagation_time*1000,3)

        bits = min(int(propagation_time*self.__bandwidth),file_bits)

        if file_bits<=bits:
            print('\tthe propagation_time between A and B is', out_time, 'ms')
            print('\tfor the bandwidth of', round(self.__bandwidth / 1000000000, 2), 'Gbps')
            print('\tbut the link never get full,')
            print('=>>\tSo the maximum number of bits in the link are {} bits({}Mbits)\n'.format(bits,round(bits/1000000,1)))
        else:
            print('\tthe propagation_time between A and B is',out_time,'ms')
            print('\tfor the bandwidth of',round(self.__bandwidth/1000000000,2),'Gbps')
            print('=>>\tthe maximum number of bits in the link are ',bits,'bits','(',round(bits/1000000,1),'Mbits)\n')
        return bits

    def bit_width(self):
        width = round(self.__light_speed/self.__bandwidth,2)
        print('\tbit width = light_speed/bandwidth')
        print('=>>\tthe width (in meters) of a bit in the link is', width, 'm\n')
        return width

    def time_total(self,bits=0):
        if  bits<=0:
            pass
        elif bits>0:
            transmission_time = bits/self.__bandwidth
            propagation_time = self.__distance/self.__light_speed
            time = round((transmission_time+propagation_time)*1000,3)
            print('\tbetween A and B, send the file of {} bits continuously:'.format(bits))
            print('\ttransmission time is {:.3f} ms'.format(transmission_time*1000))
            print('\tpropagation time is {:.3f} ms'.format(propagation_time*1000))
            print('=>>\tSo,the total time is {:.3f} ms \n'.format(time))
        return time

#默认参数为
'''
distance=50000000米,
bandwidth=2000000000bps,
light_speed=200000000m/s,可自行传入修改
'''

test1 = Transmission()
#将题干格式化输出
test1.__str__()

#第一题：求传输Xbits的文件时，链接上的最大比特数
print('Quest3-1:')
test1.max_bits(1000)#1000bits
test1.max_bits(123456789000)#123456789000bits(约124Gbits)

#第二题：求链接上的1比特所占物理长度
print('Quest3-2:')
test1.bit_width()

#第三题：求连续传输一个Xbits的文件所花的时间
print('Quest3-3:')
test1.time_total(1000)#1000bits
test1.time_total(123456789000)#123456789000bits(约124Gbits)
