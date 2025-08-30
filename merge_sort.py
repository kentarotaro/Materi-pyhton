def merged_sorted(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2 # len a = 4, mid = 2

    left_half = arr[ :mid] #[4,2]
    right_half = arr[mid:] #[1,3]

    left_sorted = merged_sorted(left_half) #[4] dan [1]
    right_sorted = merged_sorted(right_half) #[2] dan [3]

    return merge(left_sorted, right_sorted) # input ini baru akan memanggil variabel di atas
    
def merge(left, right): # fungsi akan menerima informasi di atas
    merged_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]: # membandingkan 4 dan 2 karena 4 lebih besar maka false
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    while i < len(left):
        merged_list.append(left[i])
        i += 1


    while j < len(right):
        merged_list.append(right[j])
        j += 1

    # hasil pertama dari fungsi ini adalah [2,4] dan [1,3]
    #ingat bahwa hasil di atas masih masuk ke dalam left sorted = [2,4] dan right sorted = [1,3]
    #karena return merge di bawah memanggi nilai left and right sorted maka fungsi akan jalan lagi dan menghasilkan [1,2,3,4]
    #setelah ini fungsi sudah selesai karena nilai akan kembali sebagai merged list bukan variabel yang lain

    return merged_list


a = [4,2,1,3]

print(merged_sorted(a))
