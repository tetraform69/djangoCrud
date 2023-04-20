function modal(id){
    Swal.fire({
        title: 'Eliminar Producto',
        text: 'Seguro de eliminar?',
        icon: 'warning',
        showCancelButton: true,
        cancelButtonText: 'No',
        confirmButtonText: 'Si'
    }).then((result) => {
        if (result.isConfirmed){
            location.href = `/deleteProducto/${id}`
        }
    })
}

console.log("pizza con piña");