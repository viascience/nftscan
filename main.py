import requests
import typer

app = typer.Typer()


@app.command()
def main(
    image: str, algorithm: str = None, address: str = "127.0.0.1", port: int = 5000
):
    """
    NFT scan will look for malware given the image name. The image is expected to be in data directory.

    Optionally the specific algorithm to scan for images can be defined.

    By default it will communicate through address localhost and port 5000
    """

    if algorithm is None:
        params = {"image": image}
    else:
        params = {"image": image, "algorithm": algorithm}

    response = requests.get(f"http://{address}:{port}", params=params)

    if "malware" in response.json():
        malware = response.json()["malware"]

        typer.echo(f"NFT {image}, malware detected: {malware}.")
        typer.echo("\n")
        typer.echo(f"Results from individual algorithms:")
        for algorithm_response in response.json()["info"]:
            typer.echo(f"Service: {algorithm_response['service']}")
            if "stderr" in algorithm_response["stdout"]:
                typer.echo(f"Result:\nStdout: {algorithm_response['stdout']['stdout']}")
                typer.echo(f"Stderr: {algorithm_response['stdout']['stderr']}")
            else:
                typer.echo(f"Result: {algorithm_response['stdout']}")
    else:
        typer.echo(f"Info after error: {response.json()['info']}")


if __name__ == "__main__":
    app()
