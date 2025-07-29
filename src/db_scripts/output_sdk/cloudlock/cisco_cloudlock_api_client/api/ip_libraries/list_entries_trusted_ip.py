from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ip_collection import IPCollection
from ...models.list_entries_trusted_ip_response_400 import ListEntriesTrustedIpResponse400
from ...models.list_entries_trusted_ip_response_401 import ListEntriesTrustedIpResponse401
from ...models.list_entries_trusted_ip_response_403 import ListEntriesTrustedIpResponse403
from ...models.list_entries_trusted_ip_response_404 import ListEntriesTrustedIpResponse404
from ...models.list_entries_trusted_ip_response_500 import ListEntriesTrustedIpResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["q"] = q

    params["name"] = name

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ip/trusted",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        IPCollection,
        ListEntriesTrustedIpResponse400,
        ListEntriesTrustedIpResponse401,
        ListEntriesTrustedIpResponse403,
        ListEntriesTrustedIpResponse404,
        ListEntriesTrustedIpResponse500,
    ]
]:
    if response.status_code == 200:
        response_200 = IPCollection.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ListEntriesTrustedIpResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ListEntriesTrustedIpResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ListEntriesTrustedIpResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ListEntriesTrustedIpResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ListEntriesTrustedIpResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        IPCollection,
        ListEntriesTrustedIpResponse400,
        ListEntriesTrustedIpResponse401,
        ListEntriesTrustedIpResponse403,
        ListEntriesTrustedIpResponse404,
        ListEntriesTrustedIpResponse500,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    q: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        IPCollection,
        ListEntriesTrustedIpResponse400,
        ListEntriesTrustedIpResponse401,
        ListEntriesTrustedIpResponse403,
        ListEntriesTrustedIpResponse404,
        ListEntriesTrustedIpResponse500,
    ]
]:
    """List IP Entries

     List an organization's trusted IP feeds.

    Args:
        q (Union[Unset, str]):
        name (Union[Unset, str]):
        offset (Union[Unset, str]):
        limit (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IPCollection, ListEntriesTrustedIpResponse400, ListEntriesTrustedIpResponse401, ListEntriesTrustedIpResponse403, ListEntriesTrustedIpResponse404, ListEntriesTrustedIpResponse500]]
    """

    kwargs = _get_kwargs(
        q=q,
        name=name,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    q: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        IPCollection,
        ListEntriesTrustedIpResponse400,
        ListEntriesTrustedIpResponse401,
        ListEntriesTrustedIpResponse403,
        ListEntriesTrustedIpResponse404,
        ListEntriesTrustedIpResponse500,
    ]
]:
    """List IP Entries

     List an organization's trusted IP feeds.

    Args:
        q (Union[Unset, str]):
        name (Union[Unset, str]):
        offset (Union[Unset, str]):
        limit (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[IPCollection, ListEntriesTrustedIpResponse400, ListEntriesTrustedIpResponse401, ListEntriesTrustedIpResponse403, ListEntriesTrustedIpResponse404, ListEntriesTrustedIpResponse500]
    """

    return sync_detailed(
        client=client,
        q=q,
        name=name,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    q: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        IPCollection,
        ListEntriesTrustedIpResponse400,
        ListEntriesTrustedIpResponse401,
        ListEntriesTrustedIpResponse403,
        ListEntriesTrustedIpResponse404,
        ListEntriesTrustedIpResponse500,
    ]
]:
    """List IP Entries

     List an organization's trusted IP feeds.

    Args:
        q (Union[Unset, str]):
        name (Union[Unset, str]):
        offset (Union[Unset, str]):
        limit (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IPCollection, ListEntriesTrustedIpResponse400, ListEntriesTrustedIpResponse401, ListEntriesTrustedIpResponse403, ListEntriesTrustedIpResponse404, ListEntriesTrustedIpResponse500]]
    """

    kwargs = _get_kwargs(
        q=q,
        name=name,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    q: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    offset: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        IPCollection,
        ListEntriesTrustedIpResponse400,
        ListEntriesTrustedIpResponse401,
        ListEntriesTrustedIpResponse403,
        ListEntriesTrustedIpResponse404,
        ListEntriesTrustedIpResponse500,
    ]
]:
    """List IP Entries

     List an organization's trusted IP feeds.

    Args:
        q (Union[Unset, str]):
        name (Union[Unset, str]):
        offset (Union[Unset, str]):
        limit (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[IPCollection, ListEntriesTrustedIpResponse400, ListEntriesTrustedIpResponse401, ListEntriesTrustedIpResponse403, ListEntriesTrustedIpResponse404, ListEntriesTrustedIpResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            name=name,
            offset=offset,
            limit=limit,
        )
    ).parsed
