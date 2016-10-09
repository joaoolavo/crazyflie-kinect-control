// file: listener.cpp
//
// LCM example program.
//
// compile with:
//  $ g++ -o vicon_listener vicon_listener.cpp -llcm
//
// On a system with pkg-config, you can also use:
//  $ g++ -o vicon_listener vicon_listener.cpp `pkg-config --cflags --libs lcm`
#include <sys/time.h>
#include <stdio.h>
#include <ctime>
#include <iostream>
#include <lcm/lcm-cpp.hpp>
#include "exlcm/example_t.hpp"
#include "exlcm/angle_t.hpp"
#include "vicon_t/vicon_pos_t.hpp"
#include "crazyflie_t/crazyflie_imu_t.hpp"
float pos[3], roll, pitch, yaw, timestamp, t = 0;
vicon_t::vicon_pos_t my_data;

class Handler 
{
    public:
        ~Handler() {}
        time_t timestamp;
        struct timeval td_end;
        struct timeval td_start;
        float elapsed;
        void handleMessage(const lcm::ReceiveBuffer* rbuf,
                const std::string& chan, 
                const exlcm::example_t* msg)
        {       lcm::LCM lcm1;
            pos[0] = msg->position[0];
            pos[1] = msg->position[1];          
            pos[2] = msg->position[2];

            my_data.q[0] = pos[0];
            my_data.q[1] = pos[1];
            my_data.q[2] = pos[2];
            my_data.q[3] = 0;
            my_data.q[4] = 0;
            my_data.q[5] = 0;
            //clock_t Start = clock();
            //timestamp = time (NULL);
            gettimeofday(&td_end,NULL);
            elapsed = 1000000.0 * (td_end.tv_sec -td_start.tv_sec);
            elapsed += (td_end.tv_usec - td_start.tv_usec);
            elapsed=elapsed/1000000.0;

            double time;
            time=(double)elapsed;

            // Convert time to milliseconds
            time = time*1000;
            my_data.timestamp = timestamp ;
            lcm1.publish("cf2_pete1", &my_data);
        }
};

int main(int argc, char** argv)
{
    lcm::LCM lcm;

    if(!(lcm.good()))
        return 1;

    Handler handlerObject;
    lcm.subscribe("POS_CF", &Handler::handleMessage, &handlerObject);
    
    while(0 == lcm.handle());

    return 0;
}

