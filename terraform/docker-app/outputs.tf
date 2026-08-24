output "container_id" {
  description = "Oluşturulan container'ın ID'si"
  value       = docker_container.app.id
}

output "app_url" {
  description = "API'ye erişim adresi"
  value       = "http://localhost:${var.external_port}/health"
}