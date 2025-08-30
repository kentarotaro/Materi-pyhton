# Impor deque dari library collections
from collections import deque

# format queue yaitu (current_node, path)

def bfs_template(start_node, goal_node_condition):
    """
    Template umum untuk algoritma Breadth-First Search (BFS).

    :param start_node: Titik awal pencarian.
    :param goal_node_condition: Sebuah fungsi atau lambda yang mengembalikan True jika goal tercapai.
    :return: Jalur terpendek dari start ke goal, atau None jika tidak ditemukan.
    """
    
    # 1. Inisialisasi Queue
    # Kita simpan (node_sekarang, jalur_yang_sudah_ditempuh)
    # path tidak hanya int tapi bisa juga berbentuk list dll
    queue = deque([(start_node, [start_node])])
    
    # 2. Inisialisasi 'visited'
    # Untuk menyimpan node yang sudah pernah dikunjungi agar tidak ada loop tak terbatas.
    visited = {start_node}
    
    # 3. Loop utama selama queue tidak kosong
    while queue:
        # 4. Ambil node dari paling depan antrian (FIFO)
        current_node, path = queue.popleft()
        
        # 5. Cek apakah tujuan sudah tercapai   =   
        if goal_node_condition(current_node):
            return path # Kembalikan jalur yang ditemukan
            
        # 6. Dapatkan semua "tetangga" dari node saat ini
        # Ini adalah bagian yang paling spesifik untuk setiap kasus.
        for neighbor in get_neighbors(current_node):
            
            # 7. Jika tetangga belum pernah dikunjungi
            if neighbor not in visited:
                # Tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                # Masukkan tetangga dan jalur barunya ke belakang antrian
                queue.append((neighbor, path + [neighbor]))
                
    # 8. Jika loop selesai tapi goal tidak ditemukan
    return None

# Anda harus mendefinisikan fungsi ini sesuai dengan kasus Anda
def get_neighbors(node):
    # Logika untuk mendapatkan semua node yang bisa dicapai dari 'node' saat ini.
    # Contoh: Untuk pohon, ini adalah node.left dan node.right.
    # Contoh: Untuk grid, ini adalah sel atas, bawah, kiri, kanan.
    pass