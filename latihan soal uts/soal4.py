riwayat_sekolah= [
    {
        'nama_sekolah': 'SDN 01 Aikdewa',
        'alamat_sekolah': 'Aikdewa Selatan',
        'tahun_lulus': 2016
    },
    {
        'nama_sekolah': 'SMPN 01 Pringgasela',
        'alamat_sekolah': 'Pringgasela',
        'tahun_lulus': 2019
    },
    {
        'nama_sekolah': 'SMAN 01 Pringgasela',
        'alamat_sekolah': 'Pringgasela',
        'tahun_lulus': 2022
    }
]

for riwayat in riwayat_sekolah:
    print(f"Nama Sekolah: {riwayat['nama_sekolah']}")
    print(f"Alamat Sekolah: {riwayat['alamat_sekolah']}")
    print(f"Tahun Lulus: {riwayat['tahun_lulus']}")
    print()      