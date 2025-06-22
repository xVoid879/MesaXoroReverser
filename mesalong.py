def rotate_left(x, r):
    return ((x << r) & 0xFFFFFFFFFFFFFFFF) | (x >> (64 - r))


class XoroshiroRandomSource:
    def __init__(self, seed0, seed1):
        self.s0 = seed0 & 0xFFFFFFFFFFFFFFFF
        self.s1 = seed1 & 0xFFFFFFFFFFFFFFFF

    def nextLong(self):
        result = (rotate_left((self.s0 + self.s1) & 0xFFFFFFFFFFFFFFFF, 17) + self.s0) & 0xFFFFFFFFFFFFFFFF
        s1_xor_s0 = self.s1 ^ self.s0
        self.s0 = (rotate_left(self.s0, 49) ^ s1_xor_s0 ^ ((s1_xor_s0 << 21) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF
        self.s1 = rotate_left(s1_xor_s0, 28) & 0xFFFFFFFFFFFFFFFF
        return result


def upgrade_seed_to_128bit(seed):
    HIGH_MASK = 0x6A09E667F3BCC909
    LOW_MASK = 0xBB67AE8584CAA73B
    high = seed ^ HIGH_MASK
    low = seed ^ LOW_MASK
    return high & 0xFFFFFFFFFFFFFFFF, low & 0xFFFFFFFFFFFFFFFF


def get_two_next_longs(world_seed):
    seed0, seed1 = upgrade_seed_to_128bit(world_seed)
    rng = XoroshiroRandomSource(seed0, seed1)
    first = rng.nextLong()
    second = rng.nextLong()
    return first, second


if __name__ == "__main__":
    world_seed = int(input("Enter your Minecraft world seed (64-bit integer): "))

    first_long, second_long = get_two_next_longs(world_seed)
    print(f"First nextLong():  0x{first_long:016X}")
    print(f"Second nextLong(): 0x{second_long:016X}")
