variable "external_port" {
  description = "Host tarafında API'nin yayınlanacağı port"
  type        = number
  default     = 8081
}

variable "image_tag" {
  description = "Build edilecek image'ın tag'i"
  type        = string
  default     = "devops-python-api:tf"
}

variable "container_name" {
  description = "Container'ın adı"
  type        = string
  default     = "terraform-devops-api"
}