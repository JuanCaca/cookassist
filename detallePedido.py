class Detalle_pedido():
	def __init__(self,cantidad,pedido,receta,producto):
		"""Atributos:
		self.cantidad
		self.pedido
		self.receta
		self.producto
		"""
		self.setCantidad(cantidad)
		self.setPedido(pedido)
		self.setReceta(receta) 
		self.setProducto(producto)

	def setCantidad(self,cantidad):
		self.cantidad = cantidad

	def getCantidad(self):
		return self.cantidad

	def setPedido(self,pedido):
		self.pedido = pedido

	def getPedido(self):
		return self.pedido

	def setReceta(self,receta):
		self.receta = receta

	def getReceta(self):
		return self.receta

	def setProducto(self,producto):
		self.producto = producto

	def getProducto(self):
		return self.producto
