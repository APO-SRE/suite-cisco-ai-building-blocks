from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.common_rest_error import CommonRestError
from ...types import Response


def _get_kwargs(
    fabric_id: str,
    node_id: str,
    port_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/fabrics/{fabric_id}/nodes/{node_id}/ports/{port_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CommonRestError]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
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
) -> Response[Union[Any, CommonRestError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fabric_id: str,
    node_id: str,
    port_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, CommonRestError]]:
    """Reset a specific port.

     Reset a specific port of a node in a fabric to its default values. Fabric ports cannot be reset.
    Labels and annotations are not removed.

    Args:
        fabric_id (str):
        node_id (str):
        port_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CommonRestError]]
    """

    kwargs = _get_kwargs(
        fabric_id=fabric_id,
        node_id=node_id,
        port_id=port_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fabric_id: str,
    node_id: str,
    port_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, CommonRestError]]:
    """Reset a specific port.

     Reset a specific port of a node in a fabric to its default values. Fabric ports cannot be reset.
    Labels and annotations are not removed.

    Args:
        fabric_id (str):
        node_id (str):
        port_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CommonRestError]
    """

    return sync_detailed(
        fabric_id=fabric_id,
        node_id=node_id,
        port_id=port_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    fabric_id: str,
    node_id: str,
    port_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, CommonRestError]]:
    """Reset a specific port.

     Reset a specific port of a node in a fabric to its default values. Fabric ports cannot be reset.
    Labels and annotations are not removed.

    Args:
        fabric_id (str):
        node_id (str):
        port_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CommonRestError]]
    """

    kwargs = _get_kwargs(
        fabric_id=fabric_id,
        node_id=node_id,
        port_id=port_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fabric_id: str,
    node_id: str,
    port_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, CommonRestError]]:
    """Reset a specific port.

     Reset a specific port of a node in a fabric to its default values. Fabric ports cannot be reset.
    Labels and annotations are not removed.

    Args:
        fabric_id (str):
        node_id (str):
        port_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CommonRestError]
    """

    return (
        await asyncio_detailed(
            fabric_id=fabric_id,
            node_id=node_id,
            port_id=port_id,
            client=client,
        )
    ).parsed
