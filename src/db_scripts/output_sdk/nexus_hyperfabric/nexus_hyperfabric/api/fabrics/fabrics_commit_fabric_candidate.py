from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.common_rest_error import CommonRestError
from ...models.config_commit_fabric_candidate_request import ConfigCommitFabricCandidateRequest
from ...models.config_commit_fabric_candidate_response import ConfigCommitFabricCandidateResponse
from ...types import Response


def _get_kwargs(
    fabric_id: str,
    name: str,
    *,
    body: ConfigCommitFabricCandidateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/fabrics/{fabric_id}/candidates/{name}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CommonRestError, ConfigCommitFabricCandidateResponse]]:
    if response.status_code == 200:
        response_200 = ConfigCommitFabricCandidateResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = CommonRestError.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = CommonRestError.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = CommonRestError.from_dict(response.json())

        return response_403
    if response.status_code == 429:
        response_429 = CommonRestError.from_dict(response.json())

        return response_429
    if response.status_code == 500:
        response_500 = CommonRestError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CommonRestError, ConfigCommitFabricCandidateResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fabric_id: str,
    name: str,
    *,
    client: AuthenticatedClient,
    body: ConfigCommitFabricCandidateRequest,
) -> Response[Union[CommonRestError, ConfigCommitFabricCandidateResponse]]:
    """Commit a specific candidate configuration.

     Commit a specific candidate configuration to the running configuration in a fabric.

    Args:
        fabric_id (str):
        name (str):
        body (ConfigCommitFabricCandidateRequest): The request to commit a specific candidate
            configuration of a fabric.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, ConfigCommitFabricCandidateResponse]]
    """

    kwargs = _get_kwargs(
        fabric_id=fabric_id,
        name=name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fabric_id: str,
    name: str,
    *,
    client: AuthenticatedClient,
    body: ConfigCommitFabricCandidateRequest,
) -> Optional[Union[CommonRestError, ConfigCommitFabricCandidateResponse]]:
    """Commit a specific candidate configuration.

     Commit a specific candidate configuration to the running configuration in a fabric.

    Args:
        fabric_id (str):
        name (str):
        body (ConfigCommitFabricCandidateRequest): The request to commit a specific candidate
            configuration of a fabric.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, ConfigCommitFabricCandidateResponse]
    """

    return sync_detailed(
        fabric_id=fabric_id,
        name=name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    fabric_id: str,
    name: str,
    *,
    client: AuthenticatedClient,
    body: ConfigCommitFabricCandidateRequest,
) -> Response[Union[CommonRestError, ConfigCommitFabricCandidateResponse]]:
    """Commit a specific candidate configuration.

     Commit a specific candidate configuration to the running configuration in a fabric.

    Args:
        fabric_id (str):
        name (str):
        body (ConfigCommitFabricCandidateRequest): The request to commit a specific candidate
            configuration of a fabric.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, ConfigCommitFabricCandidateResponse]]
    """

    kwargs = _get_kwargs(
        fabric_id=fabric_id,
        name=name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fabric_id: str,
    name: str,
    *,
    client: AuthenticatedClient,
    body: ConfigCommitFabricCandidateRequest,
) -> Optional[Union[CommonRestError, ConfigCommitFabricCandidateResponse]]:
    """Commit a specific candidate configuration.

     Commit a specific candidate configuration to the running configuration in a fabric.

    Args:
        fabric_id (str):
        name (str):
        body (ConfigCommitFabricCandidateRequest): The request to commit a specific candidate
            configuration of a fabric.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, ConfigCommitFabricCandidateResponse]
    """

    return (
        await asyncio_detailed(
            fabric_id=fabric_id,
            name=name,
            client=client,
            body=body,
        )
    ).parsed
