# MotoSentinel

Raspberry Pi powered sensors rig for generating ride statistics (cars / bikes)

---

### Parts
- 1x Raspberry Pi 3 / 4 / Zero.
- 1x I2C hub splitter.
- 1x DFRobot I2C Current Sensor.
- 1x ADXL345 accelerometer.
- 1x L3GD20 gyro.
- 1x AHTx0 temperature and humidity sensor.

### Setup

1. Setup Docker container:
   1. Build image: 
   ```
   sudo docker build -t motosentinel .
   ```
   2. Run container:
   ```
   sudo docker run --privileged -d \
    -p 8080:8080 \
    -v <path_to_data_dir_on_rpi>:/MotoSentinel/data \
    -v /etc/timezone:/etc/timezone:ro \
    -v /etc/localtime:/etc/localtime:ro \
    --name motosentinel motosentinel
   ```
   3. Make container auto startup:
   ```
   sudo docker update --restart unless-stopped motosentinel
   ```