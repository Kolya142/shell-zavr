mkdir /tmp/tjNVdPJEjvP1JgYT1bVq
echo I2luY2x1ZGUgPHN0ZGlvLmg+CgppbnQgbWFpbigpIHsKICAgIHByaW50Zigid29ya3MhXG4iKTsKfQ== | base64 -d > /tmp/tjNVdPJEjvP1JgYT1bVq/test.c
echo Z2NjIHRlc3QuYyAtbyB0ZXN0Lm8KLi90ZXN0Lm8= | base64 -d > /tmp/tjNVdPJEjvP1JgYT1bVq/run.sh
cd /tmp/tjNVdPJEjvP1JgYT1bVq
bash run.sh
rm -rdf /tmp/tjNVdPJEjvP1JgYT1bVq