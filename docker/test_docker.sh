docker build -t loco-mujoco:test -f docker/Dockerfile.eval .
docker run -it --rm loco-mujoco:test \
    python3 /src/examples/replay_datasets/replay_Unitree_H1.py