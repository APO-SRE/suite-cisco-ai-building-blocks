from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ip_collection import IPCollection
from ...models.list_entries_ip_suspicious_response_400 import ListEntriesIpSuspiciousResponse400
from ...models.list_entries_ip_suspicious_response_401 import ListEntriesIpSuspiciousResponse401
from ...models.list_entries_ip_suspicious_response_403 import ListEntriesIpSuspiciousResponse403
from ...models.list_entries_ip_suspicious_response_404 import ListEntriesIpSuspiciousResponse404
from ...models.list_entries_ip_suspicious_response_500 import ListEntriesIpSuspiciousResponse500
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
        "url": "/ip/suspicious",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        ListEntriesIpSuspiciousResponse400,
        ListEntriesIpSuspiciousResponse401,
        ListEntriesIpSuspiciousResponse403,
        ListEntriesIpSuspiciousResponse404,
        ListEntriesIpSuspiciousResponse500,
        list["IPCollection"],
    ]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = IPCollection.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ListEntriesIpSuspiciousResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ListEntriesIpSuspiciousResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ListEntriesIpSuspiciousResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ListEntriesIpSuspiciousResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ListEntriesIpSuspiciousResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        ListEntriesIpSuspiciousResponse400,
        ListEntriesIpSuspiciousResponse401,
        ListEntriesIpSuspiciousResponse403,
        ListEntriesIpSuspiciousResponse404,
        ListEntriesIpSuspiciousResponse500,
        list["IPCollection"],
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
        ListEntriesIpSuspiciousResponse400,
        ListEntriesIpSuspiciousResponse401,
        ListEntriesIpSuspiciousResponse403,
        ListEntriesIpSuspiciousResponse404,
        ListEntriesIpSuspiciousResponse500,
        list["IPCollection"],
    ]
]:
    """List IP Suspicious Entries

     List an organization's suspicious IP feeds.

    Args:
        q (Union[Unset, str]):
        name (Union[Unset, str]):
        offset (Union[Unset, str]):
        limit (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListEntriesIpSuspiciousResponse400, ListEntriesIpSuspiciousResponse401, ListEntriesIpSuspiciousResponse403, ListEntriesIpSuspiciousResponse404, ListEntriesIpSuspiciousResponse500, list['IPCollection']]]
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
        ListEntriesIpSuspiciousResponse400,
        ListEntriesIpSuspiciousResponse401,
        ListEntriesIpSuspiciousResponse403,
        ListEntriesIpSuspiciousResponse404,
        ListEntriesIpSuspiciousResponse500,
        list["IPCollection"],
    ]
]:
    """List IP Suspicious Entries

     List an organization's suspicious IP feeds.

    Args:
        q (Union[Unset, str]):
        name (Union[Unset, str]):
        offset (Union[Unset, str]):
        limit (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListEntriesIpSuspiciousResponse400, ListEntriesIpSuspiciousResponse401, ListEntriesIpSuspiciousResponse403, ListEntriesIpSuspiciousResponse404, ListEntriesIpSuspiciousResponse500, list['IPCollection']]
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
        ListEntriesIpSuspiciousResponse400,
        ListEntriesIpSuspiciousResponse401,
        ListEntriesIpSuspiciousResponse403,
        ListEntriesIpSuspiciousResponse404,
        ListEntriesIpSuspiciousResponse500,
        list["IPCollection"],
    ]
]:
    """List IP Suspicious Entries

     List an organization's suspicious IP feeds.

    Args:
        q (Union[Unset, str]):
        name (Union[Unset, str]):
        offset (Union[Unset, str]):
        limit (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListEntriesIpSuspiciousResponse400, ListEntriesIpSuspiciousResponse401, ListEntriesIpSuspiciousResponse403, ListEntriesIpSuspiciousResponse404, ListEntriesIpSuspiciousResponse500, list['IPCollection']]]
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
        ListEntriesIpSuspiciousResponse400,
        ListEntriesIpSuspiciousResponse401,
        ListEntriesIpSuspiciousResponse403,
        ListEntriesIpSuspiciousResponse404,
        ListEntriesIpSuspiciousResponse500,
        list["IPCollection"],
    ]
]:
    """List IP Suspicious Entries

     List an organization's suspicious IP feeds.

    Args:
        q (Union[Unset, str]):
        name (Union[Unset, str]):
        offset (Union[Unset, str]):
        limit (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListEntriesIpSuspiciousResponse400, ListEntriesIpSuspiciousResponse401, ListEntriesIpSuspiciousResponse403, ListEntriesIpSuspiciousResponse404, ListEntriesIpSuspiciousResponse500, list['IPCollection']]
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
