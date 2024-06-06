docker build -t loco-mujoco:test -f docker/Dockerfile.eval .
docker run -it --rm loco-mujoco:test \
    python3 /src/loco-mujoco/examples/simple_mushroom_env/example_unitree_a1.py