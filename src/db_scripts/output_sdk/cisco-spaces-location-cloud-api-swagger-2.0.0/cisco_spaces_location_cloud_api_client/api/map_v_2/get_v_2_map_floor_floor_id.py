from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.v2_map_floor_item import V2MapFloorItem
from ...types import Response


def _get_kwargs(
    floor_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/map/floor/{floor_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, V2MapFloorItem]]:
    if response.status_code == 200:
        response_200 = V2MapFloorItem.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = Errors.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = Errors.from_dict(response.json())

        return response_403
    if response.status_code == 500:
        response_500 = Errors.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Errors, V2MapFloorItem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    floor_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Errors, V2MapFloorItem]]:
    """Get floor details like parent location hierarchy, regions, maps, zones etc. for the floor id
    specified in API request.

    Args:
        floor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, V2MapFloorItem]]
    """

    kwargs = _get_kwargs(
        floor_id=floor_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    floor_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Errors, V2MapFloorItem]]:
    """Get floor details like parent location hierarchy, regions, maps, zones etc. for the floor id
    specified in API request.

    Args:
        floor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, V2MapFloorItem]
    """

    return sync_detailed(
        floor_id=floor_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    floor_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Errors, V2MapFloorItem]]:
    """Get floor details like parent location hierarchy, regions, maps, zones etc. for the floor id
    specified in API request.

    Args:
        floor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, V2MapFloorItem]]
    """

    kwargs = _get_kwargs(
        floor_id=floor_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    floor_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Errors, V2MapFloorItem]]:
    """Get floor details like parent location hierarchy, regions, maps, zones etc. for the floor id
    specified in API request.

    Args:
        floor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, V2MapFloorItem]
    """

    return (
        await asyncio_detailed(
            floor_id=floor_id,
            client=client,
        )
    ).parsed
