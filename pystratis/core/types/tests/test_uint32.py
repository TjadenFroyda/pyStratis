import pytest
from random import choice
from pystratis.core.types import *


def test_uint32(generate_uint32):
    hex_int = generate_uint32
    uint32(hex_int)


def test_uint32_invalid_hexstring():
    letters = 'qwerty0'
    badvalue = ''.join(choice(letters) for _ in range(64))
    with pytest.raises(ValueError):
        uint32(badvalue)


def test_uint32_long_hex_overflow():
    letters = '0123456789abcdef'
    long_value = ''.join(choice(letters) for _ in range(128))
    with pytest.raises(ValueError):
        uint32(long_value)


def test_uint32_short_hex_ok():
    first_digit = '01234567'
    letters = '0123456789abcdef'
    short_value = choice(first_digit) + ''.join(choice(letters) for _ in range(6))
    uint32(short_value)


def test_uint32_try_init_nonstr(generate_uint32):
    with pytest.raises(ValueError):
        uint32(1.5)
    with pytest.raises(ValueError):
        uint32(True)
    with pytest.raises(ValueError):
        uint32([generate_uint32])
    with pytest.raises(ValueError):
        uint32({'hash': generate_uint32})
    with pytest.raises(ValueError):
        uint32(bytes(generate_uint32, 'utf-8'))


def test_uint32_add():
    a = uint32(2)
    b = uint32(5)
    assert a + b == uint32(7)
    a += b
    assert a == uint32(7)


def test_uint32_sub():
    a = uint32(9)
    b = uint32(5)
    assert a - b == uint32(4)
    a -= b
    assert a == uint32(4)


def test_uint32_mul():
    a = uint32(2)
    b = uint32(5)
    assert a * b == uint32(2*5)
    a *= b
    assert a == uint32(2*5)


def test_uint32_floordiv():
    a = uint32(20)
    b = uint32(5)
    assert a // b == uint32(20 // 5)
    a //= b
    assert a == uint32(20 // 5)


def test_uint32_pow():
    a = uint32(20)
    b = 5
    assert a ** b == uint32(20 ** 5)
    a //= b
    assert a == uint32(20 // 5)


def test_uint32_test_underflow():
    a = uint32(2)
    b = uint32(5)
    with pytest.raises(ValueError):
        a - b
    with pytest.raises(ValueError):
        uint32(-1)


def test_uint32_test_overflow():
    numbits = 32
    with pytest.raises(ValueError):
        uint32(2**numbits)
    with pytest.raises(ValueError):
        uint32(2**numbits-1) + uint32(1)
    with pytest.raises(ValueError):
        uint32(2**numbits) * uint32(2)


def test_addition_with_other_customints():
    a = int32(2**32//2-1)
    b = int64(2**64//2-1)
    c = uint32(2**32-1)
    d = uint64(2**64-1)
    e = uint128(2**128-1)
    f = uint160(2**160-1)
    g = uint256(2**256-1)
    with pytest.raises(ValueError):
        c + a
    with pytest.raises(ValueError):
        c + b
    with pytest.raises(ValueError):
        c + d
    with pytest.raises(ValueError):
        c + e
    with pytest.raises(ValueError):
        c + f
    with pytest.raises(ValueError):
        c + g


def test_subtracting_from_larger_customints_is_ok():
    a = int32(2**32//2-1)
    b = int64(2**64//2-1)
    c = uint32(2**32-1)
    d = uint64(2**64-1)
    e = uint128(2**128-1)
    f = uint160(2**160-1)
    g = uint256(2**256-1)
    a - c
    b - c
    d - c
    e - c
    f - c
    g - c
