import hashlib

def sha256_to_u64_pair(seed: int):
    """Mimics Minecraft's upgradeSeedTo128bit using SHA-256 hashing."""
    seed_bytes = seed.to_bytes(8, byteorder='big', signed=True)
    hash_bytes = hashlib.sha256(seed_bytes).digest()

    high = int.from_bytes(hash_bytes[0:8], byteorder='big')
    low = int.from_bytes(hash_bytes[8:16], byteorder='big')
    return high, low

def rotate_left(x, r):
    return ((x << r) & 0xFFFFFFFFFFFFFFFF) | (x >> (64 - r))

class Xoroshiro128PlusPlus:
    def __init__(self, seed0, seed1):
        self.s0 = seed0 & 0xFFFFFFFFFFFFFFFF
        self.s1 = seed1 & 0xFFFFFFFFFFFFFFFF

    def nextLong(self):
        result = (rotate_left((self.s0 + self.s1) & 0xFFFFFFFFFFFFFFFF, 17) + self.s0) & 0xFFFFFFFFFFFFFFFF
        s1_xor_s0 = self.s1 ^ self.s0
        self.s0 = (rotate_left(self.s0, 49) ^ s1_xor_s0 ^ ((s1_xor_s0 << 21) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF
        self.s1 = rotate_left(s1_xor_s0, 28) & 0xFFFFFFFFFFFFFFFF
        return result

def get_mesa_band_next_longs(world_seed: int):
    seed0, seed1 = sha256_to_u64_pair(world_seed)
    rng = Xoroshiro128PlusPlus(seed0, seed1)
    first = rng.nextLong()
    second = rng.nextLong()
    return first, second

if __name__ == "__main__":
    world_seed = int(input("Enter your Minecraft world seed (64-bit integer): "))
    first_long, second_long = get_mesa_band_next_longs(world_seed)
    print(f"First nextLong() (mesa band RNG):  0x{first_long:016X}")
    print(f"Second nextLong() (mesa band RNG): 0x{second_long:016X}")
