terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "app" {
  name = var.image_tag
  build {
    context    = "../../devops-python"
    dockerfile = "Dockerfile"
  }
}

resource "docker_container" "app" {
  name  = var.container_name
  image = docker_image.app.image_id
  ports {
    internal = 8000
    external = var.external_port
  }
}